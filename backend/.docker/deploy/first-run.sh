#!/bin/bash
cd /app/api
# Forzamos que Bash use las variables que inyecta Docker
# Si ORGANIZATION está vacío, usamos un valor por defecto para que no explote
: "${ORGANIZATION:=UMH}"
: "${EMAIL:=ecoe@umh.es}"
: "${OPENECOE_ADMIN_PASSWORD:=Kui0chee}"
: "${FIRSTNAME:=Open}"
: "${SURNAME:=ECOE}"
if flask virgin;
then
    echo "Iniciando configuración inicial..."
        # Usamos comillas dobles siempre para evitar errores de argumentos vacíos
        flask create_orga --name "$ORGANIZATION"
        
        flask create_user --email "$EMAIL" \
                        --password "$OPENECOE_ADMIN_PASSWORD" \
                        --name "$FIRSTNAME" \
                        --surname "$SURNAME" \
                        --organization_name "$ORGANIZATION" \
                        --admin
    flask create_orga --name $ORGANIZATION;
    flask create_user --email $EMAIL --password $OPENECOE_ADMIN_PASSWORD --name $FIRSTNAME --surname $SURNAME --organization_name $ORGANIZATION --admin;
fi;
