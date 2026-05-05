from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository, MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido

def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    controller = PedidoController(criar_pedido_use_case)
    
    controller.criar_pedido("A", 100.0, "normal")
    controller.criar_pedido("B", 200.0, "vip")
    controller.criar_pedido("C", 300.0, "premium")
    
    for p in controller.listar_pedidos():
        print(f"Cliente: {p.cliente}\nValor Original: {p.valor_original}\nValor Desconto: {p.valor_desconto()}\nValor Final: {p.valor_final()}\n\n")
    
    
if __name__ == "__main__":
    main()
    