# UUID Generator

A comprehensive Python script for generating various types of UUIDs (Universally Unique Identifiers) with both command-line and interactive interfaces.

## Features

- **Multiple UUID Types**: Supports UUID1, UUID3, UUID4, and UUID5 generation
- **Batch Generation**: Generate multiple UUIDs at once
- **Interactive Mode**: User-friendly interactive interface
- **Command-Line Interface**: Full CLI support with various options
- **File Output**: Save generated UUIDs to files
- **Input Validation**: Robust error handling and validation
- **Type Safety**: Full type hints for better code reliability
- **Performance Timing**: Shows generation time and performance metrics

## Recent Improvements (v2.0)

### 🚀 **Type Safety & Documentation**
- ✅ Added comprehensive type hints to all functions (`List[str]`, `int`, `uuid.UUID`, `None`)
- ✅ Enhanced docstrings with proper Args, Returns, and Raises sections
- ✅ Added typing imports for better IDE support and code clarity

### 🛡️ **Input Validation & Error Handling**
- ✅ Added validation to ensure `count >= 1` in all UUID generation functions
- ✅ Added `MAX_UUID_COUNT = 10000` constant to prevent memory issues
- ✅ Enhanced error messages with specific details
- ✅ Better exception handling throughout the application

### ⚙️ **Constants & Configuration**
- ✅ Added `MAX_UUID_COUNT = 10000` for reasonable generation limits
- ✅ Added `DEFAULT_OUTPUT_FILE = "uuids.txt"` for consistency
- ✅ Better separation of configuration from logic

### 📝 **Code Quality**
- ✅ Consistent parameter validation across all functions
- ✅ Clear separation of concerns with proper error handling
- ✅ Better docstring format following Python conventions
- ✅ More robust function structure

## Installation

No additional dependencies required! The script uses only Python standard library modules.

```bash
# Make the script executable
chmod +x uuid_generator.py
```

## Usage

### Interactive Mode

Run the script in interactive mode for a user-friendly experience:

```bash
python uuid_generator.py -i
# or
python uuid_generator.py --interactive
```

The interactive mode provides:
- Menu-driven UUID type selection
- Guided input for namespace-based UUIDs (UUID3/UUID5)
- Option to save results to file
- Input validation and error handling

### Command Line Interface

#### Basic Usage

```bash
# Generate a single UUID4 (default)
python uuid_generator.py

# Generate 5 random UUIDs
python uuid_generator.py -c 5

# Generate UUID1 (timestamp-based)
python uuid_generator.py -t 1 -c 3
```

#### Advanced Usage

```bash
# Generate UUID3 with custom name and namespace
python uuid_generator.py -t 3 -n "example.com" -ns dns -c 2

# Generate UUID5 and save to file
python uuid_generator.py -t 5 -n "myproject" -ns url -c 10 -o project_ids.txt

# Generate UUIDs with different namespaces
python uuid_generator.py -t 3 -n "example" -ns oid -c 5
python uuid_generator.py -t 5 -n "user123" -ns x500 -c 3
```

## Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|--------|
| `--type` | `-t` | UUID type: 1 (timestamp), 4 (random), 3 (MD5), 5 (SHA-1) | `4` |
| `--count` | `-c` | Number of UUIDs to generate (1-10000) | `1` |
| `--name` | `-n` | Name for UUID3/UUID5 generation (required for types 3&5) | - |
| `--namespace` | `-ns` | Namespace: dns, url, oid, x500 | `dns` |
| `--output` | `-o` | Output file to save UUIDs | - |
| `--interactive` | `-i` | Run in interactive mode | - |

## UUID Types Explained

### UUID1 - Timestamp and MAC Address
- **Use case**: When you need UUIDs that can be sorted chronologically
- **Format**: Based on timestamp and MAC address
- **Example**: `123e4567-e89b-12d3-a456-426614174000`

### UUID4 - Random (Most Common)
- **Use case**: General purpose, most widely used
- **Format**: Completely random
- **Example**: `550e8400-e29b-41d4-a716-446655440000`

### UUID3 - MD5 Hash Based
- **Use case**: When you need reproducible UUIDs from the same input
- **Format**: MD5 hash of namespace and name
- **Example**: `6ba7b810-9dad-11d1-80b4-00c04fd430c8`

### UUID5 - SHA-1 Hash Based
- **Use case**: Similar to UUID3 but with SHA-1 (preferred over UUID3)
- **Format**: SHA-1 hash of namespace and name
- **Example**: `6ba7b811-9dad-11d1-80b4-00c04fd430c8`

## Available Namespaces

| Namespace | Description | Use Case |
|-----------|-------------|----------|
| `dns` | Domain Name System | Domain names, hostnames |
| `url` | Uniform Resource Locator | URLs, web resources |
| `oid` | Object Identifier | ISO OIDs |
| `x500` | X.500 Distinguished Names | Directory services |

## Examples

### Generate Multiple UUID Types

```bash
# 5 random UUIDs
python uuid_generator.py -t 4 -c 5

# 3 timestamp-based UUIDs
python uuid_generator.py -t 1 -c 3

# Reproducible UUIDs for a domain
python uuid_generator.py -t 5 -n "example.com" -ns dns -c 2
```

### Save to Files

```bash
# Generate and save to custom file
python uuid_generator.py -t 4 -c 100 -o batch_ids.txt

# Generate project-specific UUIDs
python uuid_generator.py -t 5 -n "myproject-v1.0" -ns url -c 50 -o project_uuids.txt
```

## Error Handling

The script includes comprehensive error handling:

- **Count validation**: Must be between 1 and 10,000
- **Required parameters**: UUID3/UUID5 require the `--name` parameter
- **File operations**: Graceful handling of file write errors
- **Input validation**: Invalid choices are handled gracefully in interactive mode

## API Reference

### Functions

#### `generate_uuid1(count: int = 1) -> List[str]`
Generate UUID1 (MAC address and timestamp based)

**Parameters:**
- `count`: Number of UUIDs to generate (1-10000)

**Returns:**
- List of UUID1 strings

**Raises:**
- `ValueError`: If count is less than 1 or exceeds MAX_UUID_COUNT

#### `generate_uuid4(count: int = 1) -> List[str]`
Generate UUID4 (random)

**Parameters:**
- `count`: Number of UUIDs to generate (1-10000)

**Returns:**
- List of UUID4 strings

**Raises:**
- `ValueError`: If count is less than 1 or exceeds MAX_UUID_COUNT

#### `generate_uuid3(namespace: uuid.UUID, name: str, count: int = 1) -> List[str]`
Generate UUID3 (MD5 hash based)

**Parameters:**
- `namespace`: UUID namespace to use
- `name`: Base name for UUID generation
- `count`: Number of UUIDs to generate (1-10000)

**Returns:**
- List of UUID3 strings

#### `generate_uuid5(namespace: uuid.UUID, name: str, count: int = 1) -> List[str]`
Generate UUID5 (SHA-1 hash based)

**Parameters:**
- `namespace`: UUID namespace to use
- `name`: Base name for UUID generation
- `count`: Number of UUIDs to generate (1-10000)

**Returns:**
- List of UUID5 strings

## Constants

- `MAX_UUID_COUNT = 10000`: Maximum number of UUIDs that can be generated in one call
- `DEFAULT_OUTPUT_FILE = "uuids.txt"`: Default filename for output

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## File Structure

```
.
├── uuid_generator.py    # Main script
└── README.md           # This documentation
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

