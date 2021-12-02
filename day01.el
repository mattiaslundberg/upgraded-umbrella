(require 'dash)

(defun read-lines (filePath)
  "Return a list of lines of a file at filePath."
  (with-temp-buffer
    (insert-file-contents filePath)
    (split-string (buffer-string) "\n" t)))

(let* ((testinput (read-lines "./input/day01.txt"))
       (testinput (-map #'string-to-number testinput))
       ;; (testinput '(199 200 208 210 200 207 240 269 260 263))
       (pairs (-zip-lists testinput (cons 999999 testinput)))
       (increases (--filter (> (car it) (nth 1 it)) pairs)))
  (message "Part 1: %d" (length increases)))

(let* ((testinput (read-lines "./input/day01.txt"))
       (testinput (-map #'string-to-number testinput))
       ;; (testinput '(199 200 208 210 200 207 240 269 260 263))
       (triplets (-zip-lists testinput (cons 999999 testinput) (cons 99999 (cons 999999 testinput))))
       (sums (--map (-reduce #'+ it) triplets))
       (sums (cdr (cdr sums)))
       (pairs (-zip-lists sums (cons 999999 sums)))
       (increases (--filter (> (car it) (nth 1 it)) pairs)))
  ;; (message pairs)
  (message "Part 2: %d" (length increases)))
