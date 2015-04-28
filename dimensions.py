def dimensions(im):
   dimensions = im.shape
   numberRows = dimensions[0]
   numberColumns = dimensions[1]
   if len(dimensions) == 3:
      numberBands = dimensions[2]
   else:
      numberBands = 1
   dataType = im.dtype
   return numberRows, numberColumns, numberBands, dataType
