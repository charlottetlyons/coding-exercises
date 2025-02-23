package com.spring_playground.spring_playground.ioc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.spring_playground.spring_playground.ioc.IoCBean;

@Service
public class IoCService {
    @Autowired
    IoCBean bean;

    public String sayHello() {
        return this.bean.hello();
    }
}
