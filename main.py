import platform, psutil, os, time

def audit_system():
    report = []
    report.append(f"OS: {platform.system()} {platform.release()}")
    report.append(f"CPU: {platform.processor()}")
    report.append(f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
    report.append(f"Espace disque libre: {round(psutil.disk_usage('/').free / (1024 ** 3), 2)} GB")
    return report

def nettoyer_temp():
    temp_path = os.environ.get("TEMP")
    if temp_path and os.path.exists(temp_path):
        count = 0
        for root, dirs, files in os.walk(temp_path):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                    count += 1
                except:
                    continue
        return f"{count} fichiers temporaires supprimés"
    return "Aucun fichier supprimé"

def main():
    print("Analyse du système...")
    audit = audit_system()
    for line in audit:
        print(line)
    print("\\nOptimisation...")
    result = nettoyer_temp()
    print(result)
    print("\\nTerminé.")
    with open("rapport_Solenya.txt", "w", encoding="utf-8") as f:
        f.write("\\n".join(audit + ["", result]))

if __name__ == \"__main__\":
    main()
