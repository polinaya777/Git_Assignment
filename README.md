# Simple CLI Calculator App

This is a simple command-line calculator app that supports addition and subtraction operations.

## Usage

To use this app, you need to specify the operation and the two numbers as arguments.

### Addition

To add two numbers, use the `add` command:

```bash
python app.py add x y
```

Where `x` and `y` are the numbers you want to add.

### Subtraction

To subtract two numbers, use the `subtract` command:

```bash
python app.py subtract x y
```

Where `x` is the number from which you want to subtract `y`.

### Error Handling

If you specify an invalid operation, the app will print an error message and exit with a status code of 1.
