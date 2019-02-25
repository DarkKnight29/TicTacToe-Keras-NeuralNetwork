import coremltools
coreml_model = coremltools.converters.keras.convert('./TTTNN.h5')
coreml_model.author = 'DarkKnight29 (Phani Srikar)'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Model to predict user in a game of TicTacToe'
coreml_model.save('TTTNN.mlmodel')
