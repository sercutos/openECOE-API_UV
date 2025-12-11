try:
    # --- Crear ECOE ---
    cursor.execute("""
        INSERT INTO ecoe (name, id_organization, id_coordinator, status, description)
        VALUES (%s, %s, %s, %s, %s)
    """, ("ECOE2025", 2, 2, "DRAFT", "ECOE de prueba con múltiples áreas y estaciones"))
    ecoe_id = cursor.lastrowid

     # --- Crear 10 Áreas ---
    area_ids = []
    for i in range(1, 11):
        area_name = f"Área {i}"
        area_code = f"AREA{i}"
        cursor.execute("""
            INSERT INTO area (name, id_ecoe, code, weith) VALUES (%s, %s, %s, %s)
        """, (area_name, ecoe_id, area_code, 100))
        area_ids.append(cursor.lastrowid)

    # --- Crear 12 Estaciones ---
    station_ids = []
    for i in range(1, 13):
        station_name = f"Estación {i}"
        cursor.execute("""
            INSERT INTO station (name, id_ecoe, `order`, id_parent_station, id_manager)
            VALUES (%s, %s, %s, %s, %s)
        """, (station_name, ecoe_id, i, None, 1))
        station_ids.append(cursor.lastrowid)

    # --- Crear Bloques por Estación ---
    block_ids = []
    for station_id in station_ids:
        block_name = "Bloque A"
        cursor.execute("""
            INSERT INTO block (id_station, name, `order`) VALUES (%s, %s, %s)
        """, (station_id, block_name, 1))
        block_ids.append(cursor.lastrowid)

    # --- Crear 10 Preguntas por Estación, asociadas a Áreas ---
    for idx_station, station_id in enumerate(station_ids):
        block_id = block_ids[idx_station]
        for i in range(10):
            area_id = area_ids[i % len(area_ids)]  # Asociar rotativamente a las 10 áreas
            question_schema = {
                "type": "radio",
                "reference": f"Ref {i+1}",
                "description": f"Pregunta {i+1} de la estación {idx_station+1}",
                "options": [{"id_option": 1, "points": 1, "label": "Sí", "order": 1}]
            }
            cursor.execute("""
                INSERT INTO question (id_area, `order`, id_block, id_station, question_schema, max_points)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (area_id, i+1, block_id, station_id, json.dumps(question_schema), 1.0)) """

    conn.commit()
    print("Seed de ECOE completo con áreas, estaciones y preguntas.")

except mysql.connector.Error as err:
    print("Error:", err)
    conn.rollback()

finally:
    cursor.close()
    conn.close()