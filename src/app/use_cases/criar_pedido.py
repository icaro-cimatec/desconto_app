from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO

class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway) -> None:
        self.pedido_gateway = pedido_gateway
    
    def executar(self, input_dto: CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        tipo_desconto = input_dto.tipo_desconto.lower().strip()
        
        if tipo_desconto == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")
        
        pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)
        self.pedido_gateway.salvar(pedido, tipo_desconto)
        
        return CriarPedidoOutputDTO(
            input_dto.cliente,
            input_dto.valor_original,
            pedido.valor_desconto(),
            pedido.valor_final(),
            input_dto.tipo_desconto
        )
    
    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        pedidos = self.pedido_gateway.listar()
        
        lista_dto: list[CriarPedidoOutputDTO] = []

        for registro in pedidos:
            pedido = registro["pedido"]
            dto = CriarPedidoOutputDTO(
                pedido.cliente,
                pedido.valor_original,
                pedido.valor_desconto(),
                pedido.valor_final(),
                registro["tipo_desconto"]
            )
            lista_dto.append(dto)
        
        return lista_dto
    
    