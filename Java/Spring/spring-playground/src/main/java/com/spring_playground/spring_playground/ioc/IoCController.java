package com.spring_playground.spring_playground.ioc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.spring_playground.spring_playground.ioc.IoCService;

@RestController
public class IoCController {
    @Autowired
    private IoCService service;
    
    @GetMapping("/hello")
    public String hello() {
        return this.service.sayHello();
    }
}
