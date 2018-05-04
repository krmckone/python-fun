#lang racket

(define (reverse rev_list)
  (define (rev-help rev-list index new-list)
    (if (< index 0)
        new-list
        (rev-help rev-list (- index 1) (append new-list (list (list-ref rev-list index))))))
(rev-help rev_list (- (length rev_list) 1) (list)))

(define (deep-reverse initial-list)
  (define (rev-help rev-list index new-list)
    (if (< index 0)
        new-list
        (rev-help rev-list (- index 1) (append new-list (list (list-ref rev-list index))))))
  (define (deep-rev-help rev-deep-list index new-list)
    (if (< index 0)
        new-list
        (deep-rev-help initial-list
                       (- index 1)
                       (append new-list (list (rev-help (list-ref initial-list index) (- (length (list-ref initial-list index)) 1) (list)))))))
  (deep-rev-help initial-list (- (length initial-list) 1) (list)))


(define x ( list (list 1 2) (list 3 4)))

(deep-reverse x)
