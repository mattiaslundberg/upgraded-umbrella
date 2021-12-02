(require 'dash)

(defun read-lines (file-path)
  (with-temp-buffer
    (insert-file-contents file-path)
    (split-string (buffer-string) "\n" t)))

(defun parse-input (input)
  (--map (split-string it " ") input))

(defun move-down (acc amount)
  (--update-at 1 (+ (nth 1 acc) amount) acc))

(defun move-up (acc amount)
  (--update-at 1 (- (nth 1 acc) amount) acc))

(defun move-forward (acc amount)
  (--update-at 0 (+ (car acc) amount) acc))

(defun do-move (acc it)
  (let* ((direction (car it))
         (raw-amount (nth 1 it))
         (amount (string-to-number raw-amount)))
      (cond ((string-equal direction "forward") (move-forward acc amount))
            ((string-equal direction "down") (move-down acc amount))
            ((string-equal direction "up") (move-up acc amount)))))

(let* ((rawinput (read-lines "./input/day02.txt"))
       (input (parse-input rawinput))
       (location (-reduce-from #'do-move '(0 0) input))
       (result (-reduce #'* location)))
    (message "Part 1: %s" result))

(defun move-forward-2 (acc amount)
  (let* ((horizontal (+ (car acc) amount))
         (depth (nth 1 acc))
         (vertical (nth 2 acc))
         (add (* depth amount))
         (new-vertical (+ vertical add)))
    (list horizontal depth new-vertical)))

(defun do-move-2 (acc it)
  (let* ((direction (car it))
         (raw-amount (nth 1 it))
         (amount (string-to-number raw-amount)))
      (cond ((string-equal direction "forward") (move-forward-2 acc amount))
            ((string-equal direction "down") (move-down acc amount))
            ((string-equal direction "up") (move-up acc amount)))))

(let* ((rawinput (read-lines "./input/day02.txt"))
       (input (parse-input rawinput))
       (location (-reduce-from #'do-move-2 '(0 0 0) input)))
    (message "Part 2: %s" (* (nth 0 location) (nth 2 location))))
