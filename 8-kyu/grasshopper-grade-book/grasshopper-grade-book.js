function getGrade (s1, s2, s3) {
    const media = (s1+s2+s3)/3
    
    if(media >=90 && media <= 100){
      return "A"
    }
    else if(media >= 80 && media <= 90){
      return "B"
    }
    else if(media >= 70 && media <= 80){
      return "C"
    }
    else if(media >= 60 && media <= 70){
      return "D"
    }
    else {
      return "F"
    }
  }