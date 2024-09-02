def velocidad(distancia, tiempo):
  resultado = ""
  # desde aquí hacia abajo debes modificar el programa
  velocidad_kmh = (distancia / tiempo) * 36000
  velocidad_ms = (distancia * 1000) / tiempo
  resultado = f"La velocidad es {velocidad_kmh:.1f} km/h o {velocidad_ms:.1f} m/s"
  # modifica la variable resultado
  # recuerda que los datos están en las variables distancia y tiempo
  return resultado
