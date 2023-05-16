#!/bin/sh
echo ""
echo "Customers - create"
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","address":"123 Elm St"}' http://localhost:8000/customers.json
echo ""

echo ""
echo "Customers - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/customers.json
echo ""

echo ""
echo "Customers - update"
curl -X PUT -H "Content-Type: application/json" -d '{"id": 1, "name":"Juana Joe","address":"456 Hickory Lane"}' http://localhost:8000/customers/1?format=json
echo ""

echo ""
echo "Customers - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/customers.json
echo ""

echo ""
echo "Customers - delete"
curl -X DELETE -H "Content-Type: application/json" -d '{"id": 1}' http://localhost:8000/customers/1?format=json
echo ""

echo ""
echo "Customers - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/customers.json
echo ""
