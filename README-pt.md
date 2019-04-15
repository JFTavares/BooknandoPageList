# BooknandoPageList - Cria a lista de páginas para o ePub3

Este repositório contém:

- **BooknandoNumPage_v0.1.jsx**
- Plugin para o inDesign que insere um número de página em cada página para exportar para o ePub3.

- **BooknandoPageList_v0.1.zip**
- Plugin para o Sigil que cria um lista de págins no arquivo ePub exportado pelo inDesign

Os dois plugins devem ser usados ​​juntos.

## Agradecimentos

Este dois plugins são baseados nos seguintes trabalhos:
- [PageList](https://www.mobileread.com/forums/showthread.php?t=265237) by Doitsu

- [epubTools-numPage](https://github.com/civodulab/epubTools-numPage) by civodulab

## Instruções de uso

1. Faça o download ou clone o repositório no seu computador
2. Instale o plugin **BooknandoNumPage_v0.1.jsx** na pasta de plugins do inDesign. **Atenção!** No Windows 10 coloque ele dentro desta pasta: "C:\Program Files\Adobe\Adobe InDesign CC 2019\Scripts\Scripts Panel\Samples\JavaScript"
3. Instale o plugin **BooknandoPageList_v0.1.zip** no Sigil. Use a ultima versão do Sigil (0.9.13)
4. Antes de exportar o documento do inDesign para o ePub3, aplique o script BooknandoNumPage_v0.1 no documento aberto.
5. Exporte para o ePub como de costume
6. Depois de exportar e trabalhar no Sigil, use o plugin Sigil BooknandoPageList_v0.1.zip.
7. Feito! O seu pagelist foi criado!


## Importante
Estes plugins são liberados **sem garantias**.

## Problemas e limites
O plugin inDesign não aplica números nas páginas iniciais ou nas páginas em que a caixa de texto começa no meio da página. Espero resolver logo isso!


## Contato
Se você tiver problemas ou o plugin não funcionar, use os problemas do Github para indicá-los.
Eu adoro ter ideias para melhorar este trabalho.

Twitter: #JFTavares
email: fernando@booknando.com.br






