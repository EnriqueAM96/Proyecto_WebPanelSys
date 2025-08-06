from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import smtp_service, smb_service, ssh_service, ports_service, dns_service, linux_service, windows_service

app = FastAPI(title="WebPanelSys API", version="1.0")

#Habilitar CORS para poder hacer peticiones desde el frontend al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #Permite peticiones desde cualquier origen
    allow_methods=["*"], #Permite todos los métodos HTTP
    allow_headers=["*"] #Permite todos los headers personalizados
)

#Rutas de los endpoints (ha habido cambios en el enfoque del backend que hay que aplicar)
app.include_router(smtp_service.router, prefix="/api/smtp")
app.include_router(smb_service.router, prefix="/api/smb")
app.include_router(ssh_service.router, prefix="/api/ssh")
app.include_router(ports_service.router, prefix="/api/ports")
app.include_router(dns_service.router, prefix="/api/dns")
app.include_router(linux_service.router, prefix="/api/linux")
app.include_router(windows_service.router, prefix="/api/windows")