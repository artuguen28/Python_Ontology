from owlready2 import *

# Carregar a ontologia
onto_library = get_ontology("./library.owl").load()


# Consulta para encontrar os autores de uma obra
def verificar_autores(obra):

    with onto_library:

        # Carregar instancia da obra
        obra = onto_library.search_one(iri=f"*#{obra}")

        # Verificar se a obra foi encontrada
        if obra:
            autores = list(obra.escritoPor)

            # Verificar se há autores cadastrados
            if autores:

                print(f"Autores de {str(obra)[8:]}: ")
                for autor in autores:
                    print(autor.name)
            else:
                print(f"Não há autores cadastrados para a obra: {obra}")

        else:
            print(f"Obra {obra} não encontrada.")

# Consulta para encontrar os autores de uma obra
def verificar_leitores(obra):

    with onto_library:

        # Carregar instancia da obra
        obra = onto_library.search_one(iri=f"*#{obra}")

        # Verificar se a obra foi encontrada
        if obra:
            leitores = list(obra.lidoPor)

            # Verificar se há autores cadastrados
            if leitores:

                print(f"Leitores de {str(obra)[8:]}: ")
                for leitor in leitores:
                    print(leitor.name)
            else:
                print(f"Não há leitores cadastrados para a obra: {obra}")

        else:
            print(f"Obra {obra} não encontrada.")



# Consulta para encontrar os autores de uma obra
def verificar_genero(obra):

    with onto_library:

        # Carregar instancia da obra
        obra = onto_library.search_one(iri=f"*#{obra}")

        # Verificar se a obra foi encontrada
        if obra:
            generos = list(obra.pertenceGenero)

            # Verificar se há autores cadastrados
            if generos:

                print(f"Gêneros de {str(obra)[8:]}: ")
                for genero in generos:
                    print(genero.name)
            else:
                print(f"Não há gêneros associados a esta obra: {obra}")

        else:
            print(f"Obra {obra} não encontrada.")

def main():
    verificar_autores("MobileNetV2: Inverted Residuals and Linear Bottlenecks")
    print()
    verificar_leitores("Crime e Castigo")
    print()
    verificar_genero("Guerra dos Tronos")
    print()


if __name__ == "__main__":
    main()
