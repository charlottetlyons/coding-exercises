package com.spring_playground.spring_playground.examples.ioc.service;

import org.springframework.stereotype.Service;

import com.spring_playground.spring_playground.examples.ioc.component.SpringIoCBean;

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