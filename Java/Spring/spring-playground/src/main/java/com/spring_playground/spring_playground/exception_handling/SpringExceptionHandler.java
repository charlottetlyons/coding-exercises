package com.spring_playground.spring_playground.exception_handling;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class SpringExceptionHandler {
    @ExceptionHandler
    public ResponseEntity handleException(Exception e) {
        return ResponseEntity.internalServerError().body("Error: " + e.getMessage());
    }
}
