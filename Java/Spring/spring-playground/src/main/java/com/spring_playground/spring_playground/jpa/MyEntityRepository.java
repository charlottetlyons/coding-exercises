package com.spring_playground.spring_playground.jpa;

import org.springframework.data.jpa.repository.*;

public interface MyEntityRepository extends JpaRepository<MyEntity, Long> {}
