#!/usr/bin/env python3
"""
Random UUID Generator

This script generates random UUIDs based on user input.
Supports different UUID versions and batch generation.
"""

import uuid
import argparse
import sys
from typing import List, Optional

# Constants
MAX_UUID_COUNT = 10000  # Reasonable limit to prevent memory issues
DEFAULT_OUTPUT_FILE = "uuids.txt"

def generate_uuid1(count: int = 1) -> List[str]:
    """Generate UUID1 (MAC address and timestamp based)
    
    Args:
        count: Number of UUIDs to generate
        
    Returns:
        List of UUID1 strings
        
    Raises:
        ValueError: If count is less than 1
    """
    if count < 1:
        raise ValueError("Count must be at least 1")
    if count > MAX_UUID_COUNT:
        raise ValueError(f"Count cannot exceed {MAX_UUID_COUNT}")
    return [str(uuid.uuid1()) for _ in range(count)]

def generate_uuid4(count: int = 1) -> List[str]:
    """Generate UUID4 (random)
    
    Args:
        count: Number of UUIDs to generate
        
    Returns:
        List of UUID4 strings
        
    Raises:
        ValueError: If count is less than 1
    """
    if count < 1:
        raise ValueError("Count must be at least 1")
    if count > MAX_UUID_COUNT:
        raise ValueError(f"Count cannot exceed {MAX_UUID_COUNT}")
    return [str(uuid.uuid4()) for _ in range(count)]

def generate_uuid3(namespace: uuid.UUID, name: str, count: int = 1) -> List[str]:
    """Generate UUID3 (MD5 hash based)
    
    Args:
        namespace: UUID namespace to use
        name: Base name for UUID generation
        count: Number of UUIDs to generate
        
    Returns:
        List of UUID3 strings
    """
    return [str(uuid.uuid3(namespace, f"{name}_{i}")) for i in range(count)]

def generate_uuid5(namespace: uuid.UUID, name: str, count: int = 1) -> List[str]:
    """Generate UUID5 (SHA-1 hash based)
    
    Args:
        namespace: UUID namespace to use
        name: Base name for UUID generation
        count: Number of UUIDs to generate
        
    Returns:
        List of UUID5 strings
    """
    return [str(uuid.uuid5(namespace, f"{name}_{i}")) for i in range(count)]

def interactive_mode() -> None:
    """Interactive mode for UUID generation"""
    print("\n=== UUID Generator ===")
    print("Available UUID types:")
    print("1. UUID1 (MAC address and timestamp based)")
    print("2. UUID4 (random) - Most common")
    print("3. UUID3 (MD5 hash based - requires namespace and name)")
    print("4. UUID5 (SHA-1 hash based - requires namespace and name)")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nSelect UUID type (1-5): ").strip()
            
            if choice == '5':
                print("Goodbye!")
                break
                
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select 1-5.")
                continue
                
            # Get count
            try:
                count = int(input("How many UUIDs to generate? (default: 1): ") or "1")
                if count < 1:
                    print("Count must be at least 1.")
                    continue
            except ValueError:
                print("Invalid number. Using default count of 1.")
                count = 1
            
            uuids = []
            
            if choice == '1':
                uuids = generate_uuid1(count)
            elif choice == '2':
                uuids = generate_uuid4(count)
            elif choice in ['3', '4']:
                print("\nAvailable namespaces:")
                print("1. DNS namespace")
                print("2. URL namespace")
                print("3. OID namespace")
                print("4. X500 namespace")
                
                ns_choice = input("Select namespace (1-4): ").strip()
                namespaces = {
                    '1': uuid.NAMESPACE_DNS,
                    '2': uuid.NAMESPACE_URL,
                    '3': uuid.NAMESPACE_OID,
                    '4': uuid.NAMESPACE_X500
                }
                
                if ns_choice not in namespaces:
                    print("Invalid namespace choice. Using DNS namespace.")
                    namespace = uuid.NAMESPACE_DNS
                else:
                    namespace = namespaces[ns_choice]
                
                name = input("Enter name for UUID generation: ").strip()
                if not name:
                    name = "default"
                
                if choice == '3':
                    uuids = generate_uuid3(namespace, name, count)
                else:
                    uuids = generate_uuid5(namespace, name, count)
            
            print(f"\nGenerated {len(uuids)} UUID(s):")
            print("-" * 40)
            for i, uuid_str in enumerate(uuids, 1):
                print(f"{i:3d}: {uuid_str}")
            
            # Ask if user wants to save to file
            save = input("\nSave to file? (y/N): ").strip().lower()
            if save in ['y', 'yes']:
                filename = input("Enter filename (default: uuids.txt): ").strip() or "uuids.txt"
                try:
                    with open(filename, 'w') as f:
                        for uuid_str in uuids:
                            f.write(uuid_str + '\n')
                    print(f"UUIDs saved to {filename}")
                except Exception as e:
                    print(f"Error saving file: {e}")
                    
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def main() -> None:
    """Main function to handle command line arguments and orchestrate UUID generation"""
    parser = argparse.ArgumentParser(description='Generate random UUIDs')
    parser.add_argument('-t', '--type', choices=['1', '4', '3', '5'], default='4',
                       help='UUID type: 1 (timestamp), 4 (random), 3 (MD5), 5 (SHA-1)')
    parser.add_argument('-c', '--count', type=int, default=1,
                       help='Number of UUIDs to generate (default: 1)')
    parser.add_argument('-n', '--name', type=str,
                       help='Name for UUID3/UUID5 generation')
    parser.add_argument('-ns', '--namespace', choices=['dns', 'url', 'oid', 'x500'], 
                       default='dns', help='Namespace for UUID3/UUID5 (default: dns)')
    parser.add_argument('-o', '--output', type=str,
                       help='Output file to save UUIDs')
    parser.add_argument('-i', '--interactive', action='store_true',
                       help='Run in interactive mode')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
        return
    
    if args.count < 1:
        print("Error: Count must be at least 1")
        sys.exit(1)
    
    # Generate UUIDs based on type
    uuids = []
    
    if args.type == '1':
        uuids = generate_uuid1(args.count)
    elif args.type == '4':
        uuids = generate_uuid4(args.count)
    elif args.type in ['3', '5']:
        if not args.name:
            print("Error: --name is required for UUID3 and UUID5")
            sys.exit(1)
        
        namespace_map = {
            'dns': uuid.NAMESPACE_DNS,
            'url': uuid.NAMESPACE_URL,
            'oid': uuid.NAMESPACE_OID,
            'x500': uuid.NAMESPACE_X500
        }
        namespace = namespace_map[args.namespace]
        
        if args.type == '3':
            uuids = generate_uuid3(namespace, args.name, args.count)
        else:
            uuids = generate_uuid5(namespace, args.name, args.count)
    
    # Output UUIDs
    for uuid_str in uuids:
        print(uuid_str)
    
    # Save to file if specified
    if args.output:
        try:
            with open(args.output, 'w') as f:
                for uuid_str in uuids:
                    f.write(uuid_str + '\n')
            print(f"UUIDs saved to {args.output}", file=sys.stderr)
        except Exception as e:
            print(f"Error saving to file: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == '__main__':
    main()

