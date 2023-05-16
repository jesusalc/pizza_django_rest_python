#!/bin/sh
# echo ""
# echo "Pizzas - create"
# curl -X POST -H "Content-Type: application/json" -d '{"flavor":"MG","size":"SM","count":2,"orders":{"customer":"2","status":"OD"}}' http://localhost:8000/pizzas.json
# echo ""

echo ""
echo "Pizzas - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/pizzas.json
echo ""

echo ""
echo "Pizzas - update"
curl -X PUT -H "Content-Type: application/json" -d '{"flavor":"MG","size":"LG","count":10}' http://localhost:8000/pizzas/1?format=json
echo ""

echo ""
echo "Pizzas - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/pizzas.json
echo ""

echo ""
echo "Pizzas - delete"
curl -X DELETE -H "Content-Type: application/json" -d '{"id": 1}' http://localhost:8000/pizzas/1?format=json
echo ""

echo ""
echo "Pizzas - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/pizzas.json
echo ""
