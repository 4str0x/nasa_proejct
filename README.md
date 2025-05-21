<h1 align="center">🌌 NASA_API_ROVER</h1> 

> **Descrição:**  
Sistema assíncrono desenvolvido em Python para consumir a [API da NASA Mars Rover](https://api.nasa.gov/), com foco educacional na aplicação de **padrões de projeto clássicos (GoF)**.

---

## 📚 Objetivo

Este projeto tem como objetivo demonstrar o uso de **padrões de projeto de software** mantendo um código modular, escalável e reutilizável, enquanto consome a API de fotos dos rovers da NASA:

- Curiosity  
- Opportunity  
- Spirit  
- Perseverance

---

## 🧠 Padrões de Projeto Utilizados

| Padrão GoF       | Tipo           | Aplicação                                                                 |
|------------------|----------------|---------------------------------------------------------------------------|
| Strategy         | Comportamental | Diferentes estratégias de busca por fotos (sol, data, câmera, etc.)       |
| Factory Method   | Criacional     | Criação de `Client` e `RoverService` desacoplada e extensível             |
| Adapter          | Estrutural     | Adaptação da resposta da API para um formato uniforme interno             |

---

## 🧪 Exemplo de uso
```py
from factories.rover_service_factory import create_curiosity_service
import asyncio

async def main():
    service = create_curiosity_service(sol="1000", camera="fhaz")
    result = await service.get_photos()
    print(result)

asyncio.run(main())
```

## 📜 Licença
Projeto de estudo sem fins lucrativos. Uso livre para fins educacionais.
