import cv2
import numpy as np

#Video
video_path = 'video_folhas.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (600, 800))
    output = frame.copy()

    #HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Mask da folha (tons verdes/amarelados)
    lower_leaf = np.array([15, 30, 30])
    upper_leaf = np.array([85, 255, 255])
    mask_folha = cv2.inRange(hsv, lower_leaf, upper_leaf)
    folha_segmentada = cv2.bitwise_and(frame, frame, mask=mask_folha)

    #Mask tons verdes
    lower_verde = np.array([35, 40, 40])
    upper_verde = np.array([85, 255, 255])
    mask_verde = cv2.inRange(hsv, lower_verde, upper_verde)

    #Calculo das areas
    area_folha = cv2.countNonZero(mask_folha)
    area_verde = cv2.countNonZero(cv2.bitwise_and(mask_verde, mask_folha))
    pct_verde = (area_verde / area_folha) * 100 if area_folha else 0

    #Converte a folha para cinza e detecta manchas (regiões mais escuras)
    gray = cv2.cvtColor(folha_segmentada, cv2.COLOR_BGR2GRAY)
    _, mask_manchas = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    mask_manchas = cv2.morphologyEx(mask_manchas, cv2.MORPH_OPEN, kernel, iterations=1)

    #Detecta contornos de manchas
    contours, _ = cv2.findContours(mask_manchas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_filtrados = [cnt for cnt in contours if 20 < cv2.contourArea(cnt) < 3000]
    num_manchas = len(contours_filtrados)

    
    if pct_verde < 5:  #Sem verde -> severamente doente
        status = "Severamente Doente"
        cor_status = (0, 0, 255)
    elif num_manchas > 0:
        status = "Doente"
        cor_status = (0, 165, 255)
    else:
        status = "Saudavel"
        cor_status = (0, 255, 0)

    #Desenha contornos e textos
    cv2.drawContours(output, contours_filtrados, -1, (0, 0, 255), 2)
    cv2.putText(output, f"Status: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, cor_status, 2)
    cv2.putText(output, f"Verde: {pct_verde:.1f}% | Manchas: {num_manchas}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    #Mostra o video
    cv2.imshow("Deteccao em Video", output)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
