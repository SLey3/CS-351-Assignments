from click.exceptions import BadArgumentUsage
import click

def threesum(target: int, arr: list[int]) -> tuple[bool, int]:
    """
    Write a complete implementation of the brute force ThreeSum algorithm that:

    Uses three nested loops to check all possible triplets
    Ensures indices i, j, k are distinct
    Returns true/false OR returns the actual triplet (your choice, document it)
    Handles edge cases properly (array too small, null input, etc.)
    
    Requirements:
    - Include comprehensive comments explaining your approach
    - Add a counter variable to track the number of basic operations performed
    - Implement input validation
    - Provide at least 5 test cases with expected outputs
    
    Parameters:
    - :target: comparer 
    - :arr: Array of integers
    
    Returns:
    - A tuple which contains: whether a match was found, and the count of basic operations performed
    """
    # input validation
    n = len(arr)

    if n <= 2:
        raise ValueError(f"Array has to have at least 3 elements or more. Current length: {n}")
    
    # --- main operation ---
    count = 0 # count of basic operations
    
    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # increase count by one
                count += 1
                
                # add current integers together
                res = arr[i] + arr[j] + arr[k]
                
                # compare result with target
                if res == target:
                    return (True, count,)
    return (False, count,)


@click.command()
@click.argument("array", type=str)
@click.argument("target", type=int)
@click.option("--expect-err", is_flag=True, help="Whether to expect an error or not.")
def main(array: str, target: int, expect_err: bool):
    array = list(map(int, array.strip("[]").split(",")))
    
    click.echo("Running Threesum algorithm with the following parameters:\n\n")
    click.echo(f"array: {array}\n target: {target}\n expect_err: {expect_err}\n\n")
    
    try:
        match, count = threesum(target, array)
    except ValueError as err:
        if expect_err:
            click.echo("Expected error was raised. Exiting program...", color="red")
            return
        else:
            raise BadArgumentUsage(str(err))
    else:
        click.echo("Results:\n\n")
        click.echo(f"Match: {match}\n")
        click.echo(f"Count of Basic Operations: {count}")

if __name__ == '__main__':
    main()