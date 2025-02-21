package com.spring_playground.spring_playground.examples.ioc.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.spring_playground.spring_playground.examples.ioc.service.SpringIoCService;

@RestController
public class SimpleController {
    
    @Autowired
    private final SpringIoCService springIoCService;

    public SimpleController(SpringIoCService s) {
        this.springIoCService = s;
    }

    @GetMapping("/")
    public String hello() {
        return "Hello!";
    }

    @GetMapping("/do-thing")
    public String doThing() {
        return this.springIoCService.execute();
    }
}
