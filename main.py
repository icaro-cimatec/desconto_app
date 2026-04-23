from src.models.pedido import Pedido
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.repositories.pedido_repository import PedidoRepository

from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    repo = PedidoRepository()
    
    """Criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_original = 100.0 # Definindo o valor original do pedido
    
    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_original = 200.0 # Definindo o valor original do pedido
    
    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_original = 300.0 # Definindo o valor original do pedido
    
    repo.adicionar_pedido(pedido1)
    repo.adicionar_pedido(pedido2)
    repo.adicionar_pedido(pedido3)
    
    pedidos = repo.listar_pedidos()

    for pedido in pedidos:
        print(f"Cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
