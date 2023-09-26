import cv2

# Загружаем видео
video = cv2.VideoCapture('video.mp4')

# Читаем первый кадр
ret, prev_frame = video.read()

# Преобразуем кадр в оттенки серого для более эффективной обработки
prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Итерируемся по остальным кадрам видео
while True:
    # Читаем следующий кадр
    ret, curr_frame = video.read()
    if not ret:
        break
    
    # Преобразуем текущий кадр в оттенки серого
    curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    
    # Вычисляем оптический поток
    flow = cv2.calcOpticalFlowFarneback(prev_frame_gray, curr_frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Извлекаем векторы движения из потока
    flow_x = flow[:,:,0]
    flow_y = flow[:,:,1]
    
    # Вычисляем суммарные векторы движения по всем пикселям
    vector_x = flow_x.mean()
    vector_y = flow_y.mean()
    
    # Выводим векторы движения на текущем кадре (опционально)
    cv2.arrowedLine(curr_frame, (int(curr_frame.shape[1]/2), int(curr_frame.shape[0]/2)), (int(curr_frame.shape[1]/2 + vector_x), int(curr_frame.shape[0]/2 + vector_y)), (0, 0, 255), 2)
    
    # Отображаем текущий кадр с векторами движения
    cv2.imshow('Video', curr_frame)
    
    # Ждем нажатия клавиши 'q' для остановки воспроизведения
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Обновляем предыдущий кадр
    prev_frame_gray = curr_frame_gray

# Освобождаем ресурсы
video.release()
cv2.destroyAllWindows()