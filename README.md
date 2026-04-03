# nokia-service-sap-delete
nokia router altında belirli bir servis altındaki sap ların silinmesi için hazırlanmıştır..

router üzerindeki 

show service sap-using

komut çıktısını excel dosyasına kaydederek

| PortId        | SvcId | Ingress | Ing. | Egress | Egr. | Adm | Opr  |
|--------------|-------|--------|------|--------|------|-----|------|
| lag-40:1011.0 | 1234  | 54     | none | 45     | none | Up  | Down |
| lag-42:1011.0 | 1234  | 54     | none | 45     | none | Up  | Down |
| lag-44:1011.0 | 1234  | 54     | none | 45     | none | Up  | Down |

python kod çalıştırılır. jinja template dosyasına uygun olarak 

sap_delete_config.txt 

dosyasında gerekli komutlar üretilir.
