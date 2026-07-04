# Log Report Task

## Objective
Parse the provided `access.log` file and generate a JSON report named `report.json` in the working directory.

## Input
- `access.log` — a web server access log file located in `/workspace/access.log`

## Output
Create a file named:

report.json

The JSON file must contain exactly these fields:

{
  "total_requests": <integer>,
  "status_codes": {
    "200": <integer>,
    "404": <integer>,
    "500": <integer>
  },
  "unique_ips": <integer>
}

## Success Criteria

1. Generate the output file
   - A file named `report.json` must exist in `/workspace/`.

2. Include required fields
   - The file must contain:
     - `total_requests`
     - `status_codes`
     - `unique_ips`

3. Correct total request count
   - `total_requests` must equal 10

4. Correct HTTP status summary
   - `status_codes` must equal:
     {
       "200": 6,
       "404": 2,
       "500": 2
     }

5. Correct unique IP count
   - `unique_ips` must equal 4

## Notes
- Do not rename the output file.
- Ensure the JSON is valid.
- All counts must be derived from `access.log`.
