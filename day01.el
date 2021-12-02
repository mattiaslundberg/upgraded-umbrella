(require 'dash)

(defun read-lines (file-path)
  (with-temp-buffer
    (insert-file-contents file-path)
    (split-string (buffer-string) "\n" t)))

(defun read-lines-num (file-path)
  (let ((lines (read-lines file-path)))
    (-map #'string-to-number lines)))

(defun get-increases (input)
  (let* ((second (cons 9999999 input))
         (pairs (-zip-lists input second)))
      (--filter (> (car it) (nth 1 it)) pairs)))

(defun sum-sublists (lists)
  (let ((summed (--map (-reduce #'+ it) lists)))
    (cdr (cdr summed))))

(let* ((testinput (read-lines-num "./input/day01.txt"))
       (increases (get-increases testinput)))
  (message "Part 1: %d" (length increases)))

(let* ((testinput (read-lines-num "./input/day01.txt"))
       (input-one (cons 9999999 testinput))
       (input-two (cons 9999999 input-one))
       (triplets (-zip-lists testinput input-one input-two))
       (sums (sum-sublists triplets))
       (increases (get-increases sums)))
  (message "Part 2: %d" (length increases)))
