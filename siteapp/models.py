from django.db import models


class Brand(models.Model):
	name = models.CharField("Бренд", help_text="Название бренда", max_length=100)
	descr = models.TextField("Описание", help_text="Информация о бренде", blank=True)
	logo = models.ImageField("Логотип", upload_to="img/goods", help_text="Выберите файл с изображением логотипа",
								blank=True)

	class Meta:
		verbose_name = "бренд"
		verbose_name_plural = "бренды"

	def publish(self):
		self.save()

	def __str__(self):
		return self.name


class Tara(models.Model):
	brand = models.ForeignKey(Brand, help_text="Выберите бренд", on_delete=models.CASCADE, verbose_name="Бренд")
	material = models.CharField("Материал", help_text="Материал бутылки (ПЭТ, стекло...)", max_length=100)
	volume = models.DecimalField("Объем, л.", help_text="Объем бутылки, л.", max_digits=4, decimal_places=2)
	photo = models.ImageField("Фото", upload_to="img/goods", help_text="Выберите файл с изображением", blank=True)
	storage = models.TextField("Хранение", help_text="Срок и условия хранения", blank=True)
	pack_length = models.IntegerField("Длина упаковки, мм.", help_text="Длина упаковки, мм.", blank=True, null=True)
	pack_width = models.IntegerField("Ширина упаковки, мм.", help_text="Ширина упаковки, мм.", blank=True, null=True)
	pack_height = models.IntegerField("Высота упаковки, мм.", help_text="Высота упаковки, мм.", blank=True, null=True)
	pack_quant = models.IntegerField("Кол-во бутылок, шт.", help_text="Количество бутылок в упаковке, шт.", blank=True,
									 null=True)
	pack_weight = models.DecimalField("Вес упаковки, кг.", help_text="Вес брутто упаковки, кг.",
										max_digits=3, decimal_places=1, blank=True, null=True)
	pallet_length = models.DecimalField("Длина поддона, м.", help_text="Длина поддона, м.", max_digits=2, decimal_places=1,
										blank=True, null=True)
	pallet_width = models.DecimalField("Ширина поддона, м.", help_text="Ширина поддона, м.", max_digits=2, decimal_places=1,
										blank=True, null=True)
	pallet_quant = models.IntegerField("Кол-во бутылок, шт.", help_text="Количество бутылок на поддоне, шт.", blank=True, null=True)
	pallet_weight_bru = models.DecimalField("Масса брутто, кг.", help_text="Масса брутто поддона, кг.", max_digits=5,
											decimal_places=1, blank=True, null=True)
	pallet_weight_net = models.DecimalField("Масса нетто, кг.", help_text="Масса нетто поддона, кг.", max_digits=5,
											decimal_places=1, blank=True, null=True)

	class Meta:
		verbose_name = "тара"
		verbose_name_plural = "тары"

	def publish(self):
		self.save()

	def __str__(self):
		return '%s, %s, %s' % (self.brand, self.material, self.volume)


class Drink(models.Model):
	brand = models.ForeignKey(Brand, help_text="Выберите бренд", on_delete=models.CASCADE, verbose_name="Бренд")
	tara = models.ForeignKey(Tara, help_text="Выберите тару", on_delete=models.CASCADE, verbose_name="Тара")
	taste = models.CharField("Вкус", help_text="Вкус(Груша, Минеральная, Газированная и т.п.", max_length=100, blank=True)
	photo = models.ImageField("Фото", upload_to="img/goods", help_text="Выберите файл с изображением", blank=True)

	class Meta:
		verbose_name = "напиток"
		verbose_name_plural = "напитки"

	def publish(self):
		self.save()

	def __str__(self):
		return '%s, %s' % (self.tara, self.taste)
