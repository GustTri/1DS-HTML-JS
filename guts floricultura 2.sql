create database if not exists aroma_floral;
use aroma_floral;

create table flores (id INT primary key auto_increment,
                           nome VARCHAR(99) NOT NULL,
                           tipo VARCHAR(99),
                           cor VARCHAR(99),
                           preco DECIMAL(65) NOT NULL,
                           estoque INT NOT NULL,
                           data_entrada DATE
					       );
                           
CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY,
                           nome VARCHAR(100) NOT NULL,
                           telefone VARCHAR(20),
                           email VARCHAR(100),
                           endereco TEXT
                           );
                           
CREATE TABLE vendas (id INT AUTO_INCREMENT PRIMARY KEY,
                           id_cliente INT,
                           id_flor INT,
                           quantidade INT NOT NULL,
                           data_venda DATE NOT NULL,
                           total DECIMAL(65) NOT NULL,
						   FOREIGN KEY (id_cliente) REFERENCES clientes(id),
						   FOREIGN KEY (id_flor) REFERENCES flores(id)
                           );
                           
CREATE TABLE fornecedores (
                           id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
						   nome VARCHAR(100) NOT NULL,
                           telefone VARCHAR(20),
                           email VARCHAR(100),
                           endereco TEXT
						   );
                           
CREATE TABLE produtos (
                           id_produto INT AUTO_INCREMENT PRIMARY KEY,
                           nome VARCHAR(100) NOT NULL,
                           descricao TEXT,
                           preco DECIMAL(4,2) NOT NULL,
                           tipo ENUM('Flor', 'Fitas', 'Vaso', 'Adubo') NOT NULL,
                           estoque INT DEFAULT 0,
                           id_fornecedor INT,
                           FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor)
                           );

CREATE TABLE pedidos (
						    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
                            id_cliente INT,
                            data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
                            status ENUM('Pendente', 'Pago', 'Enviado', 'Cancelado') DEFAULT 'Pendente',
                            valor_total DECIMAL(4,2),
                            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
							);
                            
CREATE TABLE itens_pedido (
                            id_item INT AUTO_INCREMENT PRIMARY KEY,
                            id_pedido INT,
                            id_produto INT,
                            quantidade INT NOT NULL,
							preco_unitario DECIMAL(4,2) NOT NULL,
                            FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
                            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
                            );

CREATE TABLE itens_pedido (
                            id_item INT AUTO_INCREMENT PRIMARY KEY,
                            id_pedido INT,
                            id_produto INT,
                            quantidade INT NOT NULL,
                            preco_unitario DECIMAL(4,2) NOT NULL,
                            FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
                            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
                            );