"""Exemplo prático de demonstração do agente Copilot Studio + GitHub MCP."""

from datetime import datetime


def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Este repositório foi gerenciado por um agente via GitHub MCP."


def main() -> None:
    print(saudacao("desenvolvedor"))
    print(f"Executado em: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
