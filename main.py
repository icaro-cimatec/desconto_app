from src.models.pedido import Pedido
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.repositories.pedido_repository import PedidoRepository
from src.controller.pedido_controller import PedidoController

from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    repo = PedidoRepository()
    service = PedidoService(repo)
    controller = PedidoController(service)
    
    """Criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_original = 100.0 # Definindo o valor original do pedido
    
    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_original = 200.0 # Definindo o valor original do pedido
    
    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_original = 300.0 # Definindo o valor original do pedido
    
    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)
    
    controller.processar_pedidos()
