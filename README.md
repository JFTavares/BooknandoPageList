# BooknandoPageList - create pagelist for ePub3

This repository contain:

- **BooknandoNumPage_v0.1.jsx**: Plugin for inDesign that insert a page number in every page for export to ePub3.

- **BooknandoPageList.zip**: Plugin for Sigil that create a listPage in the ePub file exported from inDesign

The two plugins has to be used together.

## Acknowledgement

This two plugins are based in the follow plugins:
- [PageList](https://www.mobileread.com/forums/showthread.php?t=265237) by Doitsu

- [epubTools-numPage](https://github.com/civodulab/epubTools-numPage) by civodulab

## Instructions to use
1. Download or clone the repositorie
2. Install the plugin **BooknandoNumPage_v0.1.jsx** in inDesign plugin folder. **Attention!** The path in Windows 10 is "C:\Program Files\Adobe\Adobe InDesign CC 2019\Scripts\Scripts Panel\Samples\JavaScript"
3. Install the plugin **BooknandoPageList_v0.1.zip** in Sigil
4. Before export the inDesign document to ePub3 use the BooknandoNumPage_v0.1 in the open document.
5. Export to ePub as usual
6. After exporting and working on it in Sigil use the Sigil plugin BooknandoPageList_v0.1.zip.
7. Done! Your pagelist is created!

## Important
This plugins are released **without warranties**. 

## Problems and limits
The inDesign plugin do not applu numbers in inicial pages or in pages where the box text start in the middle of page. Working on it!

## Contact
If you have troubles or the plugin are no working please use the Github Issues to indicate it.
I love have ideas to improve this work.


Twitter: @JFTavares

email: fernando@booknando.com.br