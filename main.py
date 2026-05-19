from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository, MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.presenters.pedido_presenter import PedidoPresenter

def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)
    
    controller.criar_pedido("A", 100.0, "normal")
    controller.criar_pedido("B", 200.0, "vip")
    controller.criar_pedido("C", 300.0, "premium")
    
    for pedido in controller.listar_pedidos():
        print(pedido)
    
    
if __name__ == "__main__":
    main()
    