package com.spring_barebones.spring_barebones.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SimpleController {
    @GetMapping("/")
    public ResponseEntity<String> hello() {
        return ResponseEntity.ok("Hello!");
    }
}
