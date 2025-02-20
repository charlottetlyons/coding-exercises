package com.spring_playground.spring_playground.examples;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SimpleController {
    
    @Autowired
    private final SpringIocService springIoCService;

    public SimpleController(SpringIoCService s) {
        this.springIoCService = s;
    }

    @GetMapping("/")
    public String hello() {
        return "Hello!";
    }

    @GetMapping("/do-thing")
    public String hello() {
        return "Hello!";
    }
}
