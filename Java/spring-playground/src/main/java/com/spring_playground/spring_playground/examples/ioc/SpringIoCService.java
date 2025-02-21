package com.spring_playground.spring_playground.examples.ioc;

import org.springframework.stereotype.Service;

@Service
public class SpringIoCService {
    private SpringIoCBean bean;
    
    public SpringIoCService(SpringIoCBean b) {
        this.bean = b;
    }

    public String execute() {
        return this.bean.doThing();
    }
}