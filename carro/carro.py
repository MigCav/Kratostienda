class Carro:
    def __init__(self,request):
        
        self.request = request
        
        #se mantiene el id de la sesion
        self.session = request.session
        carro = self.session.get('carro')
        
        if not carro:
            carro = self.session['carro'] = {}
            
        else:
            self.carro = carro
            
    def agregar(self, producto):
        
        #verifica si el producto esta en el dic del carro
        if (str(producto.id) not in self.carro.keys()):
            
            self.carro[producto.id] = {
                'poducto_id'    :   producto.id,
                'codigo'        :   producto.codigo,
                'precio'        :   producto.precio,
                'cantidad'      :   1,
                'imagen'        :   producto.imagen.url
            }
        else:
            for key,value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad']   =   value['cantidad'] + 1
                    value['precio']     =   value['precio'] + producto.precio
                    
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session['carro']   =   self.carro
        self.session.modified   =   True
        
    def restar_producto(self, producto):
        for key,value in self.carro.items():
            if key == str(producto.id):
                
                value['cantidad']   =   value['cantidad'] - 1
                value['precio']     =   float(value['precio'] - producto.precio)
                
                if value['cantidad'] < 1 :
                    self.eliminar_producto()
            
            break
        self.guardar_carro()
        
    def eliminar_producto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            
        self.guardar_carro()
        
    def limpiar_carro(self):
        self.session['carro'] = {}
        self.guardar_carro()
        
    