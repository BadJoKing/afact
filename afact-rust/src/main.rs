use std::env;
use num::integer::div_floor;
use std::num::ParseIntError;
use std::result::Result;
fn main() {
    let args: Vec<String> = env::args().collect();
    let num_res: Result<u128,ParseIntError> = args[1].parse();
    let num_val = match num_res{
        Ok(x) => x,
        Err(error) => panic!("Yeah, I can't seem to find any valid number there. Might wanna check if you entered the right thing. Oh and here's the error message: \n\n{error}"),
    };
    afact(num_val, true, true);
}

fn afact(x: u128, deb_tog: bool, rec_tog: bool) -> i128{
    let mut tmp: u128 = x;
    let mut i: u64 = 1;
    loop{

        let g: f64 = (tmp) as f64;
        if i != 0{
            tmp = div_floor(tmp,i.into());
            let gidiv: f64 = g/(i)as f64;
            if gidiv > (tmp) as f64{
                if deb_tog == true{
                    println!("Not a Factorial. Sorry.");
                } else {
                    return 0;
                }
                if rec_tog == true{
                    let mut v:[i128; 2]  = [-3,-3];
                    let mut j: u128 = 1;
                    loop{
                        let minu:u128 = x-j;
                        let plu:u128  = x+j;

                        let c: i128 = afact(minu, false, false);
                        let b: i128 = afact(plu, false, false);
                        if minu%2 == 0 && plu%2 == 0{
                            j+=2;
                        }else {
                            j+=1;
                        }
                        if c == -2{
                        v[0] = 0;
                        } else if c>=1{
                        v[0] = c;
                        }
                        if b == -2{
                        v[1] = 0;
                        }else if b>=1{
                        v[1] = b;
                        }
                        if (v[0] != -3) || (v[1] != -3){
                            break;
                        }

                    }
                    if v.contains(&0){
                        break;
                    }

                    if (v[0] != -3) && (v[1] == -3){
                        println!("Yeah, seems like {} might be the closest to what you're looking for.",v[0]);
                    } else if (v[0] == -3) && (v[1] != -3){
                        println!("Yeah, seems like {} might be the closest to what you're looking for.", v[1]);
                    } else if (v[0] != -3) && (v[1] != -3){
                        println!("Yeah, seems like {n1} or {n2} might be the closest to what you're looking for", n1 = v[0], n2 = v[1]);
                    }
                    
                }
                break;
            }
            if tmp == 1{
                if i == 1{
                    if deb_tog == true{
                        println!("Either 0 or 1. Choose what you like more.");
                    } else {
                        return 0;
                    }
                    break;
                } else {
                    if deb_tog == true{
                        println!("Seems to be {i}.")
                    }else {
                        return i.into();
                    }
                    break;
                }
            }
        }
        i+=1;

    }

    return -3;
}
