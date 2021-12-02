(require 'dash)

(defun read-lines (file-path)
  (with-temp-buffer
    (insert-file-contents file-path)
    (split-string (buffer-string) "\n" t)))

(defun parse-input (input)
  (--map (split-string it " ") input))

(defun do-move (acc it)
  (let* ((direction (car it))
         (raw-amount (nth 1 it))
         (amount (string-to-number raw-amount)))
    (message direction)
      (cond ((string-equal direction "forward") (--update-at 0 (+ (car acc) amount) acc))
            ((string-equal direction "down") (--update-at 1 (+ (nth 1 acc) amount) acc))
            ((string-equal direction "up") (--update-at 1 (- (nth 1 acc) amount) acc)))))

(let* ((rawinput (read-lines "./input/day02.txt"))
       (input (parse-input rawinput))
       (location (-reduce-from #'do-move '(0 0) input))
       (result (-reduce #'* location)))
    (message "%s" result))
