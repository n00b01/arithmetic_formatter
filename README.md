Here’s a simple, easy-to-understand README for your `arithmetic_arranger` Python function:

---

# Arithmetic Arranger

## Description

The `arithmetic_arranger` function is designed to arrange arithmetic problems (addition and subtraction) vertically and return a formatted string. It supports two modes:

* **Basic Arrangement**: Displays the problems in a neat, vertical format.
* **With Answers**: Displays the problems with their corresponding answers.

## Function Signature

```python
def arithmetic_arranger(problems, show_answers=False):
```

## Parameters

* **problems (list)**: A list of strings, each containing an arithmetic problem (addition or subtraction) with two operands and one operator.

  Example:

  ```python
  ["3801 - 2", "123 + 49"]
  ```

* **show\_answers (bool)**: A boolean flag to specify whether to display the answers. The default is `False`.

  * If set to `True`, the function will also display the answers to the problems.
  * If set to `False`, the answers will not be included.

## Returns

* **str**: A formatted string containing the problems arranged vertically. If `show_answers` is set to `True`, the answers will also be included in the output.

## Error Handling

The function includes error handling for the following cases:

* More than 5 problems are provided:

  * Returns: `'Error: Too many problems.'`
* Invalid problem format (not containing two operands and one operator):

  * Returns: `'Error: Each problem must contain two operands and one operator'`
* Invalid operator (other than '+' or '-'):

  * Returns: `"Error: Operator must be '+' or '-'.`
* Non-digit operands:

  * Returns: `'Error: Numbers must only contain digits.'`
* Operands longer than 4 digits:

  * Returns: `'Error: Numbers cannot be more than four digits.'`

## Example

### Input:

```python
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
```

### Output:

```
   32      3801      45      123
+ 698   -    2   +  43   +  49
-----   ------   -----   -----
  730     3799      88     172
```

### Explanation:

* The problems are arranged in a vertical format.
* The answers are displayed beneath the problems when `show_answers=True`.

---

## Usage

To use the function, simply call it with a list of arithmetic problems as strings:

```python
arithmetic_arranger(["problem1", "problem2", "problem3"], show_answers=True)
```

The function will return a formatted string that arranges the problems in a neat, vertical layout.

## Contributing
Feel free to contribute by improving functionality or optimizing the code. Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
n00b01 / g3tech

## Credits
- freecodecamp
---

