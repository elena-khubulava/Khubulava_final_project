URL_SERVICE = "https://d93820ba-6269-4c6a-8c36-896188387bca.serverhub.praktikum-services.ru"
CREATE_ORDER_PATH = "/api/v1/orders"
GET_ORDER_PATH = "/v1/orders/track?t=" # в APIDOC ошибка (это отмечено в документации) и верный запрос будет такого вида /v1/orders/track?t=123456, в противном случае мы получаем всегда код 400, а не 200
