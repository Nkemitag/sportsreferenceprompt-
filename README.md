# Head-to-Head Win Matrix

This project demonstrates a simple and reliable way to generate a head-to-head
win matrix from structured JSON data representing team records against opponents.

The goal is to transform a nested data structure into a table where:
- Each row represents a team
- Each column represents an opponent
- Each cell displays the number of wins from the row team’s perspective
- Teams are not compared against themselves (shown as `--`)

## Data Structure

The input data is expected to be a dictionary where:
- Top-level keys are team abbreviations
- Each team maps to a dictionary of opponents
- Each opponent contains a win (`W`) and loss (`L`) count

Only the win value is used for display, matching the format commonly used in
head-to-head tables.

## Approach

1. Extract and sort all team identifiers to ensure consistent row and column order.
2. Print a header row containing all teams.
3. For each team:
   - Iterate over every opponent
   - Display:
     - `--` when a team is matched with itself
     - The win count when data exists
     - An empty value if no record is available

The implementation favors readability and straightforward control flow, making it
easy to validate results and adapt for other output formats such as CSV or HTML.

## Running the Script

```bash
python head_to_head.py
