#include "pembayaran.h"
#include "ui_pembayaran.h"

pembayaran::pembayaran(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::pembayaran)
{
    ui->setupUi(this);
}

pembayaran::~pembayaran()
{
    delete ui;
}
