from owlready2 import *

# Criar uma ontologia
onto_library = get_ontology("http://www.example.org/library.owl")


# Definir classes principais
class Obra(Thing):
    namespace = onto_library

class Pessoa(Thing):
    namespace = onto_library

class Genero(Thing):
    namespace = onto_library


# Definir subclasses
## Pessoa
class Autor(Pessoa):
    namespace = onto_library

class Leitor(Pessoa):
    namespace = onto_library

## Obra
class Livro(Obra):
    namespace = onto_library

class Artigo(Obra):
    namespace = onto_library


# Definir propriedades
class escritoPor(ObjectProperty):
    namespace = onto_library
    domain = [Obra]
    range = [Autor]

class lidoPor(ObjectProperty):
    namespace = onto_library
    domain = [Obra]
    range = [Leitor]

class pertenceGenero(ObjectProperty):
    namespace = onto_library
    domain = [Obra]
    range = [Genero]


# Adicionar instâncias
livro_01 = Livro("Guerra dos Tronos")
autor_01 = Livro("George R. R. Martin")
genero_01 = Genero("Fantasia")

livro_02 = Livro("Crime e Castigo")
autor_02 = Livro("Fiódor Dostoiévski")
genero_02 = Genero("Romance")

artigo_01 = Artigo("MobileNetV2: Inverted Residuals and Linear Bottlenecks")
autor_03 = Autor("Mark Sandler")
autor_04 = Autor("Andrew Howard")
autor_05 = Autor("Menglong Zhu")
genero_03 = Genero("Paper")

leitor_01 = Leitor("Arthur Uguen")
leitor_02 = Leitor("Fulano de Tal")


# Atribuir propriedades
livro_01.escritoPor.append(autor_01)
livro_02.escritoPor.append(autor_02)

artigo_01.escritoPor.append(autor_03)
artigo_01.escritoPor.append(autor_04)
artigo_01.escritoPor.append(autor_05)

livro_01.lidoPor.append(leitor_01)
livro_02.lidoPor.append(leitor_01)
artigo_01.lidoPor.append(leitor_01)

livro_02.lidoPor.append(leitor_02)
artigo_01.lidoPor.append(leitor_02)

livro_01.pertenceGenero.append(genero_01)
livro_02.pertenceGenero.append(genero_02)
artigo_01.pertenceGenero.append(genero_03)

# Salvar a ontologia
onto_library.save("library.owl", format="rdfxml")





