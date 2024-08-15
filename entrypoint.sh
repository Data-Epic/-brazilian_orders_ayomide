#!/bin/bash

# Open DuckDB CLI
/Brazil_Order_ayomide/duckdb customer_orders.duckdb

# Keep the container running
tail -f /dev/null