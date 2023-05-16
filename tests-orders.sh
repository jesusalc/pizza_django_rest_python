#!/bin/sh
echo ""
echo "Orders - create"
curl -X POST -H "Content-Type: application/json" -d '{"customer":"2","status":"OD","pizzas":[{"flavor":"MG","size":"SM","count":2},{"flavor":"MR","size":"MD","count":1}]}' http://localhost:8000/orders.json
echo ""

echo ""
echo "Orders - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/orders.json
echo ""

echo ""
echo "Orders - update"
curl -X PUT -H "Content-Type: application/json" -d '{"customer":"2","status":"DL"}' http://localhost:8000/orders/1?format=json
echo ""

echo ""
echo "Orders - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/orders.json
echo ""

echo ""
echo "Orders - delete"
curl -X DELETE -H "Content-Type: application/json" -d '{"id": 1}' http://localhost:8000/orders/1?format=json
echo ""

echo ""
echo "Orders - list"
curl -X GET -H "Content-Type: application/json"   http://localhost:8000/orders.json
echo ""

