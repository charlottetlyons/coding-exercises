package com.spring_playground.spring_playground.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SimpleController {
    
    @GetMapping("/")
    public String hello() {
        return "Hello!";
    }
}
